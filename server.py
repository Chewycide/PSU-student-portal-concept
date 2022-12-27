from website import app, db
import website.models


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)