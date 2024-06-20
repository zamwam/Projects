import os
import zipfile
import tkinter as tk
from tkinter import filedialog, Menu
import pygame
from pygame.locals import *
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image, ImageTk
import io

class MusicPlayer:
    def __init__(self, root, title="Music Player", background="#f0f0f0", text_color="black"):
        self.root = root
        self.root.title(title)
        self.root.configure(background=background)
        
        self.playlist = []
        self.current_song_index = 0
        self.autoplay = True
        self.playing = False
        self.video_playing = False
        
        # Customization options
        self.background = background
        self.text_color = text_color
        
        self.create_widgets()
        self.create_context_menu()
        
    def create_widgets(self):
        # Header Label
        header_font = ("Helvetica", 14, "bold")
        header_label = tk.Label(self.root, text="Music Player", font=header_font, bg=self.background, fg=self.text_color)
        header_label.grid(row=0, column=0, columnspan=6, pady=10)
        
        # Load Folder Button
        self.load_button = tk.Button(self.root, text="Load Folder", command=self.load_folder, font=("Helvetica", 10), bg=self.background, fg=self.text_color)
        self.load_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # Play Button
        self.play_button = tk.Button(self.root, text="Play", command=self.play, font=("Helvetica", 10), bg=self.background, fg=self.text_color)
        self.play_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        # Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, font=("Helvetica", 10))
        self.stop_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        
        # Volume Label
        self.volume_label = tk.Label(self.root, text="Volume:", font=("Helvetica", 10), bg="#f0f0f0")
        self.volume_label.grid(row=1, column=3, padx=10, pady=10)
        
        # Volume Scale
        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, font=("Helvetica", 10))
        self.volume_scale.set(50)
        self.volume_scale.grid(row=1, column=4, padx=10, pady=10, sticky="ew")
        
        # Current Song Label
        self.current_song_label = tk.Label(self.root, text="Current Song:", font=("Helvetica", 10), bg="#f0f0f0")
        self.current_song_label.grid(row=2, column=0, padx=10, pady=10)
        
        # Song Length Label
        self.song_length_label = tk.Label(self.root, text="Song Length:", font=("Helvetica", 10), bg="#f0f0f0")
        self.song_length_label.grid(row=2, column=1, padx=10, pady=10)
        
        # Cover Art Label
        self.cover_art_label = tk.Label(self.root, bg="#ffffff")
        self.cover_art_label.grid(row=3, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        
        # Progress Bar
        self.progress_bar = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, font=("Helvetica", 10), bg="#f0f0f0")
        self.progress_bar.grid(row=4, column=0, columnspan=6, padx=10, pady=10, sticky="ew")
        self.progress_bar.config(state=tk.DISABLED)
        
        # Playback Controls Frame
        playback_controls_frame = tk.Frame(self.root, bg="#f0f0f0")
        playback_controls_frame.grid(row=5, column=0, columnspan=6, pady=10)
        
        # Previous Button
        self.prev_button = tk.Button(playback_controls_frame, text="Previous", command=self.prev_song, font=("Helvetica", 10))
        self.prev_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Rewind Button
        self.rewind_button = tk.Button(playback_controls_frame, text="Rewind", command=self.rewind_song, font=("Helvetica", 10))
        self.rewind_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Forward Button
        self.forward_button = tk.Button(playback_controls_frame, text="Forward", command=self.forward_song, font=("Helvetica", 10))
        self.forward_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Next Button
        self.next_button = tk.Button(playback_controls_frame, text="Next", command=self.next_song, font=("Helvetica", 10))
        self.next_button.grid(row=0, column=3, padx=10, pady=10)
        
        # Select File Button
        self.select_file_button = tk.Button(self.root, text="Select File", command=self.select_file, font=("Helvetica", 10))
        self.select_file_button.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky="ew")
        
        # Autoplay Checkbox
        self.autoplay_var = tk.BooleanVar()
        self.autoplay_checkbox = tk.Checkbutton(self.root, text="Autoplay", variable=self.autoplay_var, font=("Helvetica", 10), bg="#f0f0f0")
        self.autoplay_checkbox.grid(row=7, column=0, columnspan=6, padx=10, pady=10, sticky="ew")
        
        # Song Listbox
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Helvetica", 10))
        self.song_listbox.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.song_listbox.bind("<Button-3>", self.on_song_listbox_right_click)
        
        # Configure Grid Layout
        self.root.grid_rowconfigure(8, weight=1)
        self.root.grid_columnconfigure(6, weight=1)
        
        # Create context menu
        self.create_context_menu()

        self.video_frame = tk.Frame(self.root, bg="#ffffff")
        self.video_frame.grid(row=3, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        
    def create_context_menu(self):
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Play", command=self.play_selected_song)
        self.context_menu.add_command(label="Delete from PC", command=self.delete_selected_song)

    def on_song_listbox_right_click(self, event):
        # Select the item under the cursor
        self.song_listbox.selection_set(self.song_listbox.nearest(event.y))
        # Display the context menu
        self.context_menu.post(event.x_root, event.y_root)
        
    def load_folder(self):
        self.load_folder_path = filedialog.askdirectory()
        if self.load_folder_path:
            audio_files = [file for file in os.listdir(self.load_folder_path) if file.endswith((".mp3", ".wav"))]
            video_files = [file for file in os.listdir(self.load_folder_path) if file.endswith((".mp4", ".avi"))]

            if audio_files or video_files:
                self.playlist = [os.path.join(self.load_folder_path, file) for file in audio_files + video_files]
                if self.playlist:
                    self.current_song_index = 0
                    self.update_song_listbox()
                    if self.current_song_index < len(self.playlist):
                        self.current_song_label.config(text="Current Song: " + os.path.basename(self.playlist[self.current_song_index]))
                    else:
                        self.current_song_label.config(text="Current Song: No songs in the playlist")
                else:
                    self.show_message("No audio or video files found in the selected folder.")
            else:
                self.show_message("No audio or video files found in the selected folder.")
        else:
            self.show_message("No folder selected.")
        
    def select_file(self):
        selected_file = filedialog.askopenfilename(initialdir=self.load_folder_path, title="Select a File", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if selected_file:
            self.playlist = [selected_file]
            self.current_song_index = 0
            self.update_song_listbox()
            self.current_song_label.config(text="Current Song: " + os.path.basename(self.playlist[self.current_song_index]))
        
    def play(self):
        if not self.playlist:
            self.show_message("No songs loaded.")
            return
        
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        try:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()
            self.playing = True
            
            audio = MP3(self.playlist[self.current_song_index])
            song_length = int(audio.info.length)
            self.song_length_label.config(text="Song Length: " + str(song_length) + " seconds")
            
            try:
                audio_tags = ID3(self.playlist[self.current_song_index])
                if 'APIC:' in audio_tags:
                    cover_art_data = audio_tags['APIC:'].data
                    cover_art_image = Image.open(io.BytesIO(cover_art_data))
                    # Resize cover art to fit within 200x200 pixels
                    cover_art_image.thumbnail((200, 200))
                    cover_art_image = ImageTk.PhotoImage(cover_art_image)
                    self.cover_art_label.config(image=cover_art_image)
                    self.cover_art_label.image = cover_art_image
            except:
                pass
                
            # Start progress bar update
            self.update_progress_bar()
            # Start updating the current song label
            self.update_current_song()
            
            # Event handler for song completion
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            self.root.bind(pygame.USEREVENT, self.on_song_end)
            
        except pygame.error as e:
            self.show_message("Error loading the selected song.")
        
    def on_song_end(self, event):
        # Called when the current song finishes playing
        self.next_song()
        
    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.autoplay = False
        
    def set_volume(self, volume):
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(int(volume) / 100)
        
    def next_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play()
        
    def prev_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
            self.play()
        
    def rewind_song(self):
        if self.playlist and pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
        
    def forward_song(self):
        if self.playlist and pygame.mixer.music.get_busy():
            new_pos = min(pygame.mixer.music.get_pos() + 10000, pygame.mixer.Sound(self.playlist[self.current_song_index]).get_length())
            pygame.mixer.music.set_pos(new_pos)
        
    def update_song_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for song in self.playlist:
            self.song_listbox.insert(tk.END, os.path.basename(song))
        
    def update_progress_bar(self):
        # Update progress bar only when the song is playing
        if self.playing:
            song_length = MP3(self.playlist[self.current_song_index]).info.length
            current_time = pygame.mixer.music.get_pos() / 1000
            progress = (current_time / song_length) * 100
            self.progress_bar.config(state=tk.NORMAL)
            self.progress_bar.set(progress)
            self.progress_bar.config(state=tk.DISABLED)
            if self.playing:
                self.root.after(1000, self.update_progress_bar)
        
    def update_current_song(self):
        # Update current song label with the name of the current song being played
        self.current_song_label.config(text="Current Song: " + os.path.basename(self.playlist[self.current_song_index]))
        # Schedule the update to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_current_song)
        
    def show_message(self, message):
        popup = tk.Tk()
        popup.title("Message")
        popup.configure(background="#f0f0f0")
        label = tk.Label(popup, text=message, font=("Helvetica", 12), bg="#f0f0f0")
        label.pack(padx=10, pady=10)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy, font=("Helvetica", 10))
        ok_button.pack(pady=5)
        popup.mainloop()
        
    def play_selected_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            self.current_song_index = selected_index[0]
            self.play()
            
    def delete_selected_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            selected_song = self.playlist.pop(selected_index[0])
            print("Are you sure? (y): ")
            rusure = input("")
            if rusure == "y" and "Y":
                os.remove(selected_song)
                self.update_song_listbox()
            elif rusure == "n" and "Y":
                self.update_song_listbox()

    def play_video(self):
        if not self.playlist:
            self.show_message("No video loaded.")
            return

        if not self.video_playing:
            video_path = self.playlist[self.current_song_index]
            try:
                pygame.init()
                pygame.display.set_caption("Video Player")
                screen = pygame.display.set_mode((640, 480))
                clock = pygame.time.Clock()
                video = pygame.movie.Movie(video_path)
                video.set_display(screen, (0, 0, 640, 480), 0)
                video.play()
                self.video_playing = True
                while video.get_busy():
                    clock.tick(30)
            except pygame.error as e:
                print("Error loading the selected video:", e)
                self.show_message("Error playing the selected video.")
                
    def stop_video(self):
        if self.video_playing:
            for widget in self.video_frame.winfo_children():
                widget.destroy()
            self.video_playing = False

root = tk.Tk()
app = MusicPlayer(root, title="", background="#07578c", text_color="white")
root.mainloop()

