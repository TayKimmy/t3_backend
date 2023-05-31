# http://127.0.0.1:8086/api/graphs/

from flask import Blueprint, jsonify, send_file, render_template_string
from flask_restful import Api, Resource
import pandas as pd
import matplotlib.pyplot as plt
import os

graph_api = Blueprint('graph_api', __name__, url_prefix='/api/graphs')
api = Api(graph_api)

# Function to read CSV file and convert it to JSON
def read_csv_file(file_url):
    df = pd.read_csv(file_url)
    return df.to_dict()

class GraphAPI:
    # API method to get all team data
    class _Read(Resource):
        def get(self):
            team_data = {}

            # Define the CSV file URLs
            csv_urls = [
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/76ers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/blazers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/bucks.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/bulls.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/cavaliers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/celtics.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/clippers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/grizzlies.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/hawks.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/heat.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/hornets.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/jazz.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/kings.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/knicks.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/lakers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/magic.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/mavericks.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/nets.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/nuggets.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/pacers.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/pelicans.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/pistons.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/raptors.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/rockets.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/spurs.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/suns.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/thunder.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/timberwolves.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/warriors.csv',
                'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/wizards.csv'
            ]

            # Read each CSV file and store the data in the team_data dictionary
            for url in csv_urls:
                team_name = os.path.splitext(os.path.basename(url))[0]
                team_data[team_name] = read_csv_file(url)

            return jsonify(team_data)

    # API method to get team data for a specific player
    class _ReadPlayer(Resource):
        def get(self, team_name, player_name):
            csv_url = f'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/{team_name}.csv'
            player_data = read_csv_file(csv_url)
            player_data_filtered = {k: v for k, v in player_data.items() if player_name in v}
            if not player_data_filtered:
                return jsonify({'message': 'Player not found'})
            return jsonify(player_data_filtered)

    api.add_resource(_Read, '/')
    api.add_resource(_ReadPlayer, '/<string:team_name>/<string:player_name>')

# Serve the CSV files
@graph_api.route('/csv/<string:team_name>')
def serve_csv(team_name):
    csv_url = f'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/{team_name}.csv'
    return send_file(csv_url, as_attachment=True)

# Route to display data in a table
@graph_api.route('/table/<string:team_name>')
def display_table(team_name):
    csv_url = f'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/{team_name}.csv'
    df = pd.read_csv(csv_url)
    column_order = ['Player', 'GP', 'Points', 'Assists', 'Rebounds', 'Steals', 'Blocks', 'FG%', '3PT%']
    df_ordered = df[column_order]
    return render_template_string(df_ordered.to_html())

# Route to display data in a bar graph
@graph_api.route('/bar_graph/<string:team_name>')
def display_bar_graph(team_name):
    csv_url = f'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/{team_name}.csv'
    df = pd.read_csv(csv_url)
    aspects = ['Points', 'Assists', 'Rebounds', 'Steals', 'Blocks', 'FG%', '3PT%']
    plt.figure(figsize=(10, 6))
    for aspect in aspects:
        plt.bar(df['Player'], df[aspect], label=aspect)
    plt.xlabel('Player')
    plt.ylabel('Value')
    plt.title(f'Player Performance - {team_name.capitalize()}')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'bar_graph_{team_name}.png')
    plt.close()
    return send_file(f'bar_graph_{team_name}.png', mimetype='image/png')

# Route to display data in a pie graph
@graph_api.route('/pie_graph/<string:team_name>')
def display_pie_graph(team_name):
    csv_url = f'https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/{team_name}.csv'
    df = pd.read_csv(csv_url)
    aspects = ['Points', 'Assists', 'Rebounds', 'Steals', 'Blocks', 'FG%', '3PT%']
    plt.figure(figsize=(8, 8))
    for aspect in aspects:
        plt.pie(df[aspect], labels=df['Player'], autopct='%1.1f%%', startangle=90)
        plt.title(f'{aspect} Distribution - {team_name.capitalize()}')
        plt.axis('equal')
        plt.savefig(f'pie_graph_{team_name}_{aspect}.png')
        plt.clf()
    return send_file(f'pie_graph_{team_name}_{aspects[-1]}.png', mimetype='image/png')


if __name__ == '__main__':
    graph_api.run()