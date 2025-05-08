# 🚨 ERIS – Emergency Response Information System

ERIS is a smart emergency response platform designed to enhance how emergencies are reported, tracked, and managed in Ghana. It connects citizens, responders, and agencies through real-time technology, helping reduce response times and save lives.

---

## 📌 Features

- 🆘 **Emergency Reporting** – Citizens can quickly report incidents (accidents, fire, medical emergencies, etc.)
- 📍 **Real-Time Location Tracking** – Accurate GPS location tagging for each incident
- 🔔 **Instant Notifications** – Responders and agencies are alerted instantly
- 📊 **Admin Dashboard** – For monitoring, analysis, and decision-making
- 👥 **User Roles** – Admins, emergency responders, and citizens
- 📂 **Incident History** – Log and manage past emergencies for data analysis
- 📡 **Multi-Agency Support** – Connects fire service, police, ambulance, and more

---

## 🛠️ Tech Stack

**Frontend**
- React.js / HTML + CSS (depending on build version)
- JavaScript
- Leaflet.js (for mapping)

**Backend**
- Python (Flask or FastAPI)
- PostgreSQL (or SQLite for testing)
- JWT (for authentication)
- RESTful API

**Others**
- Google Maps / OpenStreetMap API
- Twilio or Email API for alerts (planned)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js & npm (for React frontend)
- Git
- PostgreSQL (or SQLite for development)

### Backend Setup

```bash
git clone https://github.com/yourusername/eris.git
cd eris/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
````

### Frontend Setup (React Version)

```bash
cd eris/frontend

# Install dependencies
npm install

# Start the development server
npm start
```

---

## 🧪 Testing

* Unit and integration tests coming soon.
* Use Postman or Swagger UI for testing API endpoints.

---

## 🧑🏽‍💻 Contributing

Contributions are welcome! Whether you're fixing bugs, improving the UI, or adding new features, your help is appreciated.

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request
