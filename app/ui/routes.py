from flask import Blueprint, render_template, request, redirect
from app.models import db, Player
import pandas as pd

ui_bp = Blueprint(
   'ui_bp', __name__,
   template_folder='templates',
   static_folder='static'
)


@ui_bp.route('/')
def home():
    return render_template("home.html")


@ui_bp.route('/players', methods=['GET', 'POST'])
def players_list():
    # first = request.form.get('first')
    # last = request.form.get('last')
    # height = request.form.get('height')
    # weight = request.form.get('weight')
    # threepoint = request.form.get('threepoint')
    # freethrow = request.form.get('freethrow')
    # avgscore = request.form.get('avgscore')
    # player1 = Player(
    #     first=first,
    #     last=last,
    #     height=height,
    #     weight=weight,
    #     threepoint=threepoint,
    #     freethrow=freethrow,
    #     avgscore=avgscore
    # )
    # db.session.add(player1)
    # db.session.commit()
    return render_template('players.html', players=players)


@ui_bp.route('/players/add_player')
def add_player():
    title = 'Create New Player'
    return render_template('add_player.html', title=title)


@ui_bp.route('/players/import/upload_file', methods=['GET', 'POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv_players(uploaded_file.filename)
    return redirect('/players/import')


@ui_bp.route('/players/import', methods=['GET', 'POST'])
def import_players():
    return render_template('upload_players.html')


def parse_csv_players(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Student object for each row
    for i, row in csv_data.iterrows():
        player = Player(
            long_name=row['long_name'],
            age=row['age'],
            dob=row['dob'],
            height_cm=row['height_cm'],
            weight_kg=row['weight_kg'],
            club=row['club'],
            nationality=row['nationality'],
            overall=row['overall']
        )
        db.session.add(player)
    db.session.commit()


@ui_bp.route('/api/players')
def players():
    return {'data': [player.to_dict() for player in Player.query]}


@ui_bp.route('/players/select_players')
def view_method():
    player_list = ['Air', 'Land', 'Sea']
    players = Player.query.all()
    print(players)
    player_list = [r.long_name for r in db.session.query(Player.long_name)]
    return render_template('select_players.html', player_list=player_list)
