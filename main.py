import pandas as pd


class MusicRecommendationAI:
    def __init__(self):
        self.user_preferences = {"genres": [], "artists": [], "moods": [], "tempo": ""}

    def gather_user_preferences(self):
        self.user_preferences["genres"] = input(
            "Enter preferred genres (comma-separated): "
        ).split(",")
        self.user_preferences["artists"] = input(
            "Enter preferred artists (comma-separated): "
        ).split(",")
        self.user_preferences["moods"] = input(
            "Enter preferred moods (comma-separated): "
        ).split(",")
        self.user_preferences["tempo"] = input("Enter preferred tempo: ")

    def fetch_music_data(self):
        # Replace the link with an actual dataset link
        music_data = pd.read_csv("https://example.com/music_data.csv", encoding="utf-8")
        return music_data

    def generate_recommendations(self, music_data):
        recommendations = pd.DataFrame()
        if "Genre" in music_data:
            recommendations = music_data[
                music_data["Genre"].isin(self.user_preferences["genres"])
                & music_data["Artist"].isin(self.user_preferences["artists"])
                & music_data["Mood"].isin(self.user_preferences["moods"])
                & (music_data["Tempo"] == self.user_preferences["tempo"])
            ]
        return recommendations

    def present_recommendations(self, recommendations):
        print("Music Recommendations:")
        if recommendations.empty:
            print("No recommendations found.")
        else:
            print(recommendations)

    def run(self):
        self.gather_user_preferences()
        music_data = self.fetch_music_data()
        recommendations = self.generate_recommendations(music_data)
        self.present_recommendations(recommendations)


if __name__ == "__main__":
    recommendation_ai = MusicRecommendationAI()
    recommendation_ai.run()
