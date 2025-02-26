
# ChatterBox

A brief description of what this project does and who it's for

ChatterBox is a social media application built with Django that allows users to share quick updates—called "banters"—and connect with others through following, liking, and commenting functionalities. The application is designed to provide a lightweight, engaging platform for social interactions, making it easy to express thoughts, share moments, and stay connected with friends and new people alike.


Usage
Register & Login: Create an account to start posting banters and interacting with other users.
Update Profile: Customize your profile by uploading a profile picture, adding a bio, and linking your social media accounts.
Post Banters: Share your thoughts with the community.
Follow/Unfollow: Connect with other users and manage your social network.
Explore: Use the search functionality to find other users and banters.
Contributing
Contributions are welcome! If you have ideas for new features or find any bugs, please open an issue or submit a pull request.

Fork the repository.
Create your feature branch: git checkout -b feature/my-feature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/my-feature
Open a pull request.
## Features
- User Authentication:

    Registration & Login: New users can sign up using a custom registration form (with email, first name, last name, and username) and log in to their account.
    Profile Management: Users can update their profile with a picture, bio, and links to their website or social media (Facebook, Instagram, LinkedIn).
    Banter Posting:

    Create and post "banters" (short text updates) that appear on your timeline.
    View the latest banters from users across the platform.
    Edit or delete your own banters.
    Social Interactions:

- Follow/Unfollow: 

    Connect with other users by following them and see who follows you.
    Likes: Like banters posted by other users, with a like count displayed on each post.
    Search Functionality: Search for specific banters or users using dedicated search pages.
- Responsive UI:

    Designed with Bootstrap for a modern, mobile-friendly interface.
    Clean, intuitive layout for browsing profiles, banters, and social connections.

Technologies Used

- Backend:
    Django – Python-based web framework for rapid development and clean design.
    Frontend:

-   HTML5, CSS3, Bootstrap – For responsive and modern UI.
-   JavaScript and Bootstrap JS – For dynamic components (like - - dropdown menus and tabs).
- Font Awesome – For icons used in social links and action buttons.
-   Other Tools:
    Django Forms – Custom forms for user registration, profile updates, and banter posting.
    Django Messages Framework – For providing feedback on actions like posting, following, or logging in.



## Technologies Used


- Backend:
    Django – Python-based web framework for rapid development and clean design.
    Frontend:

-   HTML5, CSS3, Bootstrap – For responsive and modern UI.
-   JavaScript and Bootstrap JS – For dynamic components (like - - dropdown menus and tabs).
- Font Awesome – For icons used in social links and action buttons.
-   Other Tools:
    Django Forms – Custom forms for user registration, profile updates, and banter posting.
    Django Messages Framework – For providing feedback on actions like posting, following, or logging in.

## Installation

Install my-project with npm

1. Clone the repository:

```
git clone https://github.com/yourusername/chatterbox.git
cd chatterbox

```
2. Set up a virtual environment:

```
python3 -m venv venv
# On MAC : source venv/bin/activate  
# On Windows: venv\Scripts\activate

```
3. Install dependencies:

```
pip install -r requirements.txt

```
4. Apply migrations:

```
python manage.py migrate

```
5. Create a superuser (optional, for admin access):
```
python manage.py createsuperuser

```
6. Run the development server:
```
python manage.py runserver
```

7. Open your browser and navigate to:

http://127.0.0.1:8000

    
## Usage

- Register & Login: Create an account to start posting banters and interacting with other users.
- Update Profile: Customize your profile by uploading a profile picture, adding a bio, and linking your social media accounts.
- Post Banters: Share your thoughts with the community.
- Follow/Unfollow: Connect with other users and manage your social network.
- Explore: Use the search functionality to find other users and banters.




## Contributing

Contributions are welcome! If you have ideas for new features or find any bugs, please open an issue or submit a pull request.

Fork the repository.

- Create your feature branch: `git checkout -b feature/my-feature`
- Commit your changes: `git commit -m 'Add some feature'`
- Push to the branch: `git push origin feature/my-feature`
- Open a pull request.

## License

[MIT](https://github.com/rinkesh18/ChatterBox-django/blob/main/LICENSE)
