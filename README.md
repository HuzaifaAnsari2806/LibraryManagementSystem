# Library Management System

A web-based Library Management System to manage books efficiently.

## Features
- User authentication and authorization
- Book catalog management
- Borrow and return books

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** MySQL

## Installation

### Prerequisites
- Python 3.10+
- MySQL
- Git

### Backend Setup
```sh
# Clone the repository
git clone https://github.com/HuzaifaAnsari2806/LibraryManagementSystem.git
cd LibraryManagementSystem/backend

# Create a virtual environment and activate it
python -m venv penv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

# Configure database in settings.py

# Run migrations
```sh
python manage.py migrate

# Start the development server
python manage.py runserver
```


## Usage
- API is available at `http://localhost:8000/api/`.
- Use admin credentials to access the dashboard.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries, contact [Huzaifa Ansari](https://github.com/HuzaifaAnsari2806).
