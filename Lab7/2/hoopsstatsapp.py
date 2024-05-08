"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd


def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")

    def cleanStats(frame):
        newframe = pd.read_csv('cleanbrogdonstats.csv')
        newframe.drop(columns=["FG","3PT", "FT"], inplace=True)
        
        frame[["FGM", "FGA"]] = frame.FG.str.split("-", expand=True)
        field_goals_made = frame["FGM"]
        newframe.insert(2, "FGM", field_goals_made)
        field_goals_attempt = frame["FGA"]
        newframe.insert(3, "FGA", field_goals_attempt)

        frame[["3PM", "3PA"]] = frame["3PT"].str.split("-", expand=True)
        three_points_made = frame["3PM"]
        newframe.insert(5, "3PM", three_points_made)
        three_points_attempt = frame["3PA"]
        newframe.insert(6, "3PA", three_points_attempt)

        frame[["FTM", "FTA"]] = frame["FT"].str.split("-", expand=True)
        free_throws_made = frame["FTM"]
        newframe.insert(8, "FTM", free_throws_made)
        free_throws_attempt = frame["FTA"]
        newframe.insert(9, "FTA", free_throws_attempt)

        return newframe

    cleaned_frame=cleanStats(frame)

    hoop_stats_view = HoopStatsView(cleaned_frame)

    hoop_stats_view.mainloop()

if __name__ == "__main__":
    main()
