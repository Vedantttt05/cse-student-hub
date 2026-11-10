# CSE Student Hub 🎓

A Python and Streamlit-based academic productivity application designed to help Computer Science Engineering students organize their academic activities in one place.

## 🚀 Features

### 1. Assignment Management
- Add and manage assignments.
- Track assignment completion.
- Store assignment details using SQLite.

### 2. Notes Management
- Create and store academic notes.
- Search and filter notes.
- Edit and delete existing notes.

### 3. Project Tracker
- Add and manage academic projects.
- Track project status and priority.
- Store technologies used.
- Monitor project progress and deadlines.

### 4. Interactive Dashboard
- Assignment statistics.
- Project status visualization.
- Upcoming deadlines.
- Project progress tracking.
- Academic activity summary.

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- Git and GitHub

## 📁 Project Structure

```text
CSE-Student-Hub/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── db.py
│
├── pages/
│   ├── assignments.py
│   ├── notes.py
│   └── projects.py
│
└── assets/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vedantttt05/cse-student-hub.git
```

### 2. Navigate into the project

```bash
cd cse-student-hub
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🗄️ Database

The application uses SQLite for local data storage.

The database is created and initialized by the application. Local database files are excluded from Git using `.gitignore`.

## 🔮 Future Improvements

- User authentication and registration.
- AI-powered study assistant.
- AI-generated study schedules.
- Calendar integration.
- Attendance management.
- Cloud database integration.
- Deployment on Streamlit Community Cloud.

## 👨‍💻 Author

**Vedant**

GitHub: [@Vedantttt05](https://github.com/Vedantttt05)

## 📜 License

This project is available for educational and learning purposes.