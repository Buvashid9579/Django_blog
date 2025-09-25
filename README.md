Django Dynamic Blog Platform 📝
This project is a comprehensive, full-stack blog application built from the ground up using Python and the Django web framework. It is designed to provide a seamless and interactive experience for both content creators and readers, featuring a robust user authentication system, complete post management, and a dynamic commenting section.

The application serves as a practical demonstration of modern web development principles, including Model-View-Template (MVT) architecture, database management with an ORM, and user session handling.

✨ Key Features in Detail
👤 Full User Authentication: A secure and complete user authentication system.

Users can register for a new account with a unique username and password.

Existing users can log in and log out, with sessions managed by Django.

Users can view and update their own profile information.

✍️ Rich Post Management: Full CRUD (Create, Read, Update, Delete) functionality for blog posts, with author-specific permissions.

Logged-in users can create new posts using a simple form.

The homepage displays a paginated list of all posts for easy browsing.

Authors can edit or delete their own posts, but not the posts of other users.

🖼️ Image Uploads: The platform supports image uploads to make blog posts more engaging.

Integrated with Django's ImageField, which uses the Pillow library to handle image processing and storage.

Images are automatically uploaded and linked to their corresponding posts.

💬 Interactive Commenting: A dynamic comment section is available on each post's detail page.

Only registered and logged-in users can write comments, preventing spam.

Comments are displayed chronologically, fostering community discussion.

📱 Responsive & Clean UI: The frontend is built with a mobile-first approach to ensure a great user experience on any device, from desktops to smartphones.

⚙️ Powerful Admin Panel: The project leverages the built-in Django Admin interface, allowing a site administrator (superuser) to easily manage users, posts, and comments.

🛠️ Technology Stack
Component	Technology
Backend	Python, Django
Frontend	HTML5, CSS3, JavaScript
Database	SQLite 3 (for development)
Image Handling	Pillow

🚀 Getting Started
To get a local copy up and running, follow these simple steps.

1. Clone the Repository

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Set Up the Environment
Create a virtual environment and install all the necessary dependencies from the requirements.txt file.

Bash

# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Set Up the Database
Apply the database migrations to create the necessary tables.

Bash

python manage.py makemigrations
python manage.py migrate
4. Run the Server
Start the Django development server.

Bash

python manage.py runserver
The application will be running at http://127.0.0.1:8000/. You can access the admin panel at http://127.0.0.1:8000/admin/ after creating a superuser (python manage.py createsuperuser).



Version Control	Git & GitHub
Environment	venv (Python Virtual Environment)
