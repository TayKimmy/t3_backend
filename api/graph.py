from flask import Blueprint, jsonify, send_file, render_template_string
from flask_restful import Api, Resource
import pandas as pd
import matplotlib.pyplot as plt

graph_api = Blueprint('graph_api', __name__, url_prefix='/api/graphs')
api = Api(graph_api)

# Read the Lakers CSV file
df = pd.read_csv('https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/lakers.csv')

class GraphAPI:
    # API method to get all Lakers data
    class _Read(Resource):
        def get(self):
            return jsonify(df.to_dict())

    # API method to get Lakers data for a specific player
    class _ReadPlayer(Resource):
        def get(self, player_name):
            player_data = df[df['Player'] == player_name]
            if player_data.empty:
                return jsonify({'message': 'Player not found'})
            return jsonify(player_data.to_dict())

    api.add_resource(_Read, '/')
    api.add_resource(_ReadPlayer, '/<string:player_name>')

# Serve the Lakers CSV file
@graph_api.route('/csv')
def serve_csv():
    return send_file('https://raw.githubusercontent.com/TayKimmy/t3_backend/main/api/lakers.csv', as_attachment=True)

# Route to display data in a table
@graph_api.route('/table')
def display_table():
    column_order = ['Player', 'GP', 'Points', 'Assists', 'Rebounds', 'Steals', 'Blocks', 'FG%', '3PT%']

    # Reorder the columns in the DataFrame
    df_ordered = df[column_order]

    # Convert the reordered DataFrame to a dictionary
    data_dict = df_ordered.to_dict(orient='list')

    # Create a new dictionary with the desired column order
    reordered_dict = {column: data_dict[column] for column in column_order}

    return render_template_string(df.to_html())

# Route to display data in a bar graph
@graph_api.route('/bar_graph')
def display_bar_graph():
    plt.figure(figsize=(10, 6))
    plt.bar(df['Player'], df['Points'])
    plt.xlabel('Player')
    plt.ylabel('Points')
    plt.title('Lakers Points Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('bar_graph.png')
    plt.close()
    return send_file('bar_graph.png', mimetype='image/png')

# Route to display data in a pie graph
@graph_api.route('/pie_graph')
def display_pie_graph():
    plt.figure(figsize=(8, 8))
    plt.pie(df['Points'], labels=df['Player'], autopct='%1.1f%%')
    plt.title('Lakers Points Distribution')
    plt.savefig('pie_graph.png')
    plt.close()
    return send_file('pie_graph.png', mimetype='image/png')

if __name__ == '__main__':
    graph_api.run()