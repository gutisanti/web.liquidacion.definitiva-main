import sys
sys.path.append("src")
from view_web.flask_app import Run

if __name__ == "__main__":
    Run.app.run(debug=True)