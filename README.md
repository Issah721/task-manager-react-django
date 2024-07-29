# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Running the Application Locally

Follow these steps to set up and run the application on your local machine.

### 1. **Clone the Repository**

First, clone the repository from GitHub:

```bash
git clone https://github.com/Issah721/task-manager-react-django.git
```

### 2. **Navigate to the Project Directory**

Change into the project directory:

```bash
cd task-manager-react-django
```

### 3. **Set Up a Virtual Environment**

Create and activate a virtual environment (if using `pipenv`):

```bash
pipenv shell
```

### 4. **Install Dependencies**

Install the required dependencies using `pipenv`:

```bash
pipenv install
```

### 5. **Apply Migrations**

Apply the database migrations to set up the database schema:

```bash
python manage.py migrate
```

### 6. **Create a Superuser (Optional)**

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### 7. **Run the Development Server**

Start the development server:

```bash
python manage.py runserver
```

The server will start and you can access the application at `http://localhost:8000`.

### 8. **Access the Admin Interface (Optional)**

If you created a superuser, you can access the Django admin interface at:

```
http://localhost:8000/admin
```

### 9. **Testing (Optional)**

Run the test suite to ensure everything is working correctly:

```bash
python manage.py test
```

### 10. **Stop the Server**

To stop the server, simply press `Ctrl+C` in your terminal.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

# API Documentation

## Overview

This documentation provides details on the API endpoints for the backend project built with Django REST framework. It includes information on how to interact with the API, including available endpoints, request/response formats, and example requests.

## Installation and Setup

1. **Install Dependencies**
   Install the required packages using Pipenv:
   ```bash
   pipenv install djangorestframework django-cors-headers
   ```

2. **Add to Installed Apps**
   Ensure that `rest_framework` and `corsheaders` are added to the `INSTALLED_APPS` in your Django settings:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'corsheaders',
       ...
   ]
   ```

3. **Add Middleware**
   Add `corsheaders.middleware.CorsMiddleware` to the `MIDDLEWARE` setting in your Django settings:
   ```python
   MIDDLEWARE = [
       ...
       'corsheaders.middleware.CorsMiddleware',
       ...
   ]
   ```

4. **Configure CORS**
   Set up CORS settings in your Django settings:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",
       "https://your-frontend-domain.com",
   ]
   ```

## Authentication

Authentication is handled using token-based authentication. You need to include the token in the `Authorization` header of your requests.

### Request Header
```http
Authorization: Token your-auth-token
```

## Endpoints

### 1. **List Items**

- **Endpoint:** `/api/items/`
- **Method:** `GET`
- **Description:** Retrieve a list of all items.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Item 1",
      "description": "Description of Item 1"
    },
    {
      "id": 2,
      "name": "Item 2",
      "description": "Description of Item 2"
    }
  ]
  ```

### 2. **Create Item**

- **Endpoint:** `/api/items/`
- **Method:** `POST`
- **Description:** Create a new item.
- **Request Body:**
  ```json
  {
    "name": "New Item",
    "description": "Description of New Item"
  }
  ```
- **Response:**
  ```json
  {
    "id": 3,
    "name": "New Item",
    "description": "Description of New Item"
  }
  ```

### 3. **Retrieve Item**

- **Endpoint:** `/api/items/{id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific item.
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Item 1",
    "description": "Description of Item 1"
  }
  ```

### 4. **Update Item**

- **Endpoint:** `/api/items/{id}/`
- **Method:** `PUT`
- **Description:** Update the details of a specific item.
- **Request Body:**
  ```json
  {
    "name": "Updated Item",
    "description": "Updated Description"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Updated Item",
    "description": "Updated Description"
  }
  ```

### 5. **Delete Item**

- **Endpoint:** `/api/items/{id}/`
- **Method:** `DELETE`
- **Description:** Delete a specific item.
- **Response:**
  ```json
  {
    "message": "Item deleted successfully."
  }
  ```

## Example Requests

### List Items

**Request:**
```http
GET /api/items/ HTTP/1.1
Host: api.your-domain.com
Authorization: Token your-auth-token
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Item 1",
    "description": "Description of Item 1"
  },
  {
    "id": 2,
    "name": "Item 2",
    "description": "Description of Item 2"
  }
]
```

### Create Item

**Request:**
```http
POST /api/items/ HTTP/1.1
Host: api.your-domain.com
Authorization: Token your-auth-token
Content-Type: application/json

{
  "name": "New Item",
  "description": "Description of New Item"
}
```

**Response:**
```json
{
  "id": 3,
  "name": "New Item",
  "description": "Description of New Item"
}
```

## Error Handling

Errors will be returned in the following format:
```json
{
  "detail": "Error message"
}
```

**Example:**
```json
{
  "detail": "Invalid authentication token."
}
```

Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Configuration

After downloading the files, move the `todo` file to the `backend` directory and place the `src` and `public` folders into the `frontend` directory.

## Video Overview

Check out this video overview for a detailed demonstration of the project here: [https://www.awesomescreenshot.com/video/29966643?key=6644a17c947ea45c8be2ab76040fa75a]
