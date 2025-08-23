# AI Video Generator 🎥

A modern web application that generates videos from text prompts using AI technology. This project leverages Google's Veo-3 model for video generation and AWS S3 for video storage, providing a simple and intuitive interface for users to create AI-generated videos with just a text prompt.

## ✨ Features

- Text-to-video generation using Google's Veo-3 model
- Simple, intuitive web interface
- Automatic video storage and serving via AWS S3
- Fast API backend with CORS support
- Easily deployable to cloud platforms

## 🏗️ Project Structure

```
AI-video-gen/
├── frontend/                # Frontend static website
│   ├── index.html          # Main HTML page with UI
│   ├── vercel.json         # Vercel configuration for API proxying(not in git)
│   └── .vercel/            # Vercel deployment files(not in git)
│
└── backend/                 # FastAPI backend service
    ├── app/
    │   ├── main.py         # FastAPI application setup
    │   ├── routes.py       # API route definitions
    │   └── utils.py        # Video generation and S3 upload utilities
    ├── .env                # Environment variables (not in git)
    ├── requirements.txt    # Python dependencies
```

## 🚀 Installation and Setup

### Prerequisites

- Python 3.8+
- Node.js (for local frontend development)
- AWS account with S3 bucket
- Google AI API key (for Veo-3 model)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/poornachandra-sarasAI/AI-video-gen.git
   cd AI-video-gen/backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory:
   ```
   GOOGLE_API_KEY=your_google_api_key
   AWS_REGION=your_aws_region
   S3_BUCKET_NAME=your_s3_bucket_name
   ```

5. Run the backend:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Serve the frontend locally (using any static file server):
   ```bash
   # Using Python's built-in server
   python -m http.server 5000
   
   # Or using Node's serve package
   npx serve
   ```

3. Open your browser and navigate to `http://localhost:5000`

## 🔑 API Key Management

This project requires the following API keys and credentials:

1. **Google AI API Key**: Used for accessing the Veo-3 model for video generation
2. **AWS Credentials**: For uploading videos to S3 (either via environment variables or IAM roles)

These keys should be stored in the `.env` file in the backend directory and should **never** be committed to version control.

## 🖥️ Local Development

### Backend Development

The backend is built with FastAPI, which provides automatic API documentation. After starting the backend server, navigate to `http://localhost:8000/docs` to explore the API endpoints interactively.

### Frontend Development

The frontend is a simple HTML/CSS/JavaScript application that can be modified directly and served using any static file server.

## 🏛️ Architecture

The application follows a simple client-server architecture:

1. **Frontend**: Static HTML/JS/CSS website that provides the user interface
   - Sends prompts to the backend API
   - Displays the generated video

2. **Backend**: FastAPI application that handles:
   - API request/response handling
   - Integration with Google AI for video generation
   - Uploading videos to AWS S3
   - Returning public URLs to the frontend


3. **External Services**:
   - **Google Veo-3**: Generates videos from text prompts
   - **AWS S3**: Stores and serves the generated videos

### API Flow

1. User enters a prompt in the frontend
2. Frontend sends a POST request to `/generate` endpoint
3. Backend processes the request:
   - Calls Google Veo-3 API to generate a video
   - Saves the video temporarily
   - Uploads the video to S3
   - Returns the public URL to the frontend
4. Frontend displays the video to the user

## 🌐 Deployment

### Backend Deployment

The backend is deployed on an EC2 virtual machine, which is serving the API. As EC2 and S3 belong to AWS, an internal IAM Role was enough to handle smooth upload and retrieval from S3 bucket using EC2. 

### Frontend Deployment

The frontend is already configured for deployment on Vercel:

1. Connect your repository to Vercel
2. Configure the environment variables if needed
3. Deploy

The included `vercel.json` file sets up the API proxying to your backend server.

## 👥 Contribution

Contributions are welcome! Here's how you can contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.