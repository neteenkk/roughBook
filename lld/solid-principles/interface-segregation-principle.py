from abc import ABC, abstractmethod

# Audio-only capabilities
class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

    @abstractmethod
    def stop_audio(self):
        pass

    @abstractmethod
    def adjust_audio_volume(self, volume):
        pass



# video-only capabilities

class VideoPlayerControls(ABC):
    @abstractmethod
    def player_video(self, video_file):
        pass

    @abstractmethod
    def stop_video(self):
        pass

    @abstractmethod
    def adjust_video_brightness(self, brightness):
        pass


class ModernAudioPlayer(AudioPlayer):
    def play_audio(self, audio_file):
        print(f"ModernAudioPlayer: Playing Audio {audio_file}")


    def stop_audio(self):
        print("ModernAudioPlayer: Audio Stopped")

    def adjust_audio_volume(self, volume):
        print(f"ModernAudioPlayer: volume set to {volume}")


if __name__ == "__main__":
    audioPlayer = ModernAudioPlayer()
    audioPlayer.play_audio("low_fade.mp3")
    audioPlayer.adjust_audio_volume(23)
