# Django Channels Real-Time Chat Application

This project is a real-time chat application built with Django Channels, Redis, and ReactJS. It enables users to engage in chat conversations with real-time updates.

## Setup

### Backend

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/django-channels-chatapp.git
   cd django-channels-chatapp
   ```

2. **Create Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start Django Development Server:**

   ```bash
   python manage.py runserver
   ```

### Frontend

1. **Navigate to Frontend Directory:**

   ```bash
   cd frontend
   ```

2. **Install Node Dependencies:**

   ```bash
   npm install
   ```

3. **Start React Development Server:**

   ```bash
   npm start
   ```

## Usage

- Open your web browser and access `http://localhost:3000`.
- Create Django users using `python manage.py createsuperuser`.
- Log in with different users in separate browsers.
- Enter a username and chat room.
- Start sending and receiving real-time messages.
