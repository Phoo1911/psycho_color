# Psycho-Color Analysis System: Deployment Guide

## Overview

This guide provides instructions for deploying the Psycho-Color Analysis System in various environments. The system can be deployed as a standalone web application, integrated into existing websites, or set up as an API service.

## Prerequisites

Before deployment, ensure you have the following:

- Python 3.10 or higher
- Node.js 14 or higher (for UI development and building)
- pip (Python package manager)
- npm (Node.js package manager)
- Git (for version control)
- Access to an LLM provider (OpenAI, Anthropic, etc.)

## Deployment Options

### Option 1: Standalone Web Application

This option deploys the complete system as a standalone web application.

#### Step 1: Clone the Repository

```bash
git clone https://github.com/your-organization/psycho-color-analysis.git
cd psycho-color-analysis
```

#### Step 2: Set Up Python Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 3: Configure LLM Integration

Create a `.env` file in the root directory:

```
LLM_PROVIDER=openai  # or anthropic, etc.
LLM_API_KEY=your_api_key_here
LLM_MODEL=gpt-4  # or claude-2, etc.
```

#### Step 4: Build the Frontend

```bash
cd frontend
npm install
npm run build
cd ..
```

#### Step 5: Start the Application

```bash
# Development mode
python app.py

# Production mode with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

The application will be available at `http://localhost:8000` (or the configured port).

### Option 2: Static Website Deployment

This option deploys just the frontend as a static website, using the API as a separate service.

#### Step 1: Build the Frontend

```bash
cd frontend
npm install
npm run build
```

#### Step 2: Configure API Endpoint

Edit the `frontend/src/config.js` file to point to your API endpoint:

```javascript
export const API_ENDPOINT = 'https://your-api-endpoint.com/api';
```

#### Step 3: Deploy to Web Server

Copy the contents of the `frontend/build` directory to your web server's document root.

For Nginx:
```bash
cp -r frontend/build/* /var/www/html/
```

For Apache:
```bash
cp -r frontend/build/* /var/www/html/
```

#### Step 4: Configure Web Server

For Nginx, create a configuration file `/etc/nginx/sites-available/psycho-color`:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

Enable the site:
```bash
ln -s /etc/nginx/sites-available/psycho-color /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

### Option 3: API Service Deployment

This option deploys just the backend as an API service.

#### Step 1: Set Up Python Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 2: Configure LLM Integration

Create a `.env` file in the root directory:

```
LLM_PROVIDER=openai  # or anthropic, etc.
LLM_API_KEY=your_api_key_here
LLM_MODEL=gpt-4  # or claude-2, etc.
```

#### Step 3: Deploy as API Service

For production deployment, we recommend using Gunicorn with Nginx:

```bash
# Install Gunicorn
pip install gunicorn

# Start Gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 api:app
```

Configure Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name api.your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Option 4: Docker Deployment

This option uses Docker for containerized deployment.

#### Step 1: Build Docker Image

Create a `Dockerfile` in the root directory:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build frontend
RUN apt-get update && apt-get install -y nodejs npm
RUN cd frontend && npm install && npm run build

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

Build the image:
```bash
docker build -t psycho-color-analysis .
```

#### Step 2: Run Docker Container

```bash
docker run -d -p 8000:8000 --name psycho-color-analysis \
  -e LLM_PROVIDER=openai \
  -e LLM_API_KEY=your_api_key_here \
  -e LLM_MODEL=gpt-4 \
  psycho-color-analysis
```

### Option 5: Cloud Platform Deployment

#### AWS Elastic Beanstalk

1. Install the EB CLI:
   ```bash
   pip install awsebcli
   ```

2. Initialize EB application:
   ```bash
   eb init -p python-3.10 psycho-color-analysis
   ```

3. Create an environment:
   ```bash
   eb create psycho-color-analysis-env
   ```

4. Set environment variables:
   ```bash
   eb setenv LLM_PROVIDER=openai LLM_API_KEY=your_api_key_here LLM_MODEL=gpt-4
   ```

5. Deploy:
   ```bash
   eb deploy
   ```

#### Google Cloud Run

1. Build and push Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/your-project/psycho-color-analysis
   ```

2. Deploy to Cloud Run:
   ```bash
   gcloud run deploy psycho-color-analysis \
     --image gcr.io/your-project/psycho-color-analysis \
     --platform managed \
     --set-env-vars LLM_PROVIDER=openai,LLM_API_KEY=your_api_key_here,LLM_MODEL=gpt-4
   ```

#### Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Deploy to Heroku:
   ```bash
   heroku create psycho-color-analysis
   heroku config:set LLM_PROVIDER=openai LLM_API_KEY=your_api_key_here LLM_MODEL=gpt-4
   git push heroku main
   ```

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Port for the web server | `8000` |
| `LLM_PROVIDER` | LLM provider (openai, anthropic, etc.) | `openai` |
| `LLM_API_KEY` | API key for LLM provider | None (required) |
| `LLM_MODEL` | Model to use for analysis | `gpt-4` |
| `DEBUG` | Enable debug mode | `False` |
| `LOG_LEVEL` | Logging level | `INFO` |

### Configuration File

For more advanced configuration, create a `config.py` file:

```python
# LLM Configuration
LLM_CONFIG = {
    'provider': 'openai',
    'api_key': 'your_api_key_here',
    'model': 'gpt-4',
    'temperature': 0.7,
    'max_tokens': 1000
}

# Analysis Configuration
ANALYSIS_CONFIG = {
    'enable_jung_energies': True,
    'enable_personality_dimensions': True,
    'enable_emotional_tendencies': True,
    'enable_contextual_analysis': True
}

# API Configuration
API_CONFIG = {
    'rate_limit': 100,  # requests per hour
    'enable_caching': True,
    'cache_ttl': 3600  # seconds
}

# UI Configuration
UI_CONFIG = {
    'enable_animations': True,
    'enable_dark_mode': True,
    'default_language': 'en'
}
```

## Scaling Considerations

### Horizontal Scaling

For high-traffic deployments, consider:

1. Deploying multiple instances behind a load balancer
2. Using a distributed cache (Redis, Memcached) for session data
3. Implementing a queue system for LLM requests (RabbitMQ, Redis)

### Vertical Scaling

For resource-intensive operations:

1. Increase CPU and memory allocation for LLM processing
2. Optimize database queries and indexing
3. Implement efficient caching strategies

### Cost Optimization

To optimize costs:

1. Implement caching for common analysis patterns
2. Use smaller LLM models for initial analysis, larger models for detailed insights
3. Batch LLM requests when possible
4. Implement tiered service levels based on usage patterns

## Monitoring and Maintenance

### Logging

Configure logging to track system performance and errors:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Health Checks

Implement a health check endpoint:

```python
@app.route('/health')
def health_check():
    return {
        'status': 'healthy',
        'version': '1.0.0',
        'llm_provider_status': check_llm_provider()
    }
```

### Backup and Recovery

1. Regularly backup configuration and custom data
2. Implement automated deployment pipelines for quick recovery
3. Document recovery procedures for different failure scenarios

## Security Hardening

### API Security

1. Implement API key authentication
2. Use HTTPS for all communications
3. Implement rate limiting to prevent abuse
4. Validate and sanitize all input data

### Data Protection

1. Encrypt sensitive data at rest and in transit
2. Implement proper access controls
3. Regularly audit data access and usage
4. Comply with relevant data protection regulations

## Troubleshooting

### Common Issues

1. **LLM API Connection Failures**
   - Check API key validity
   - Verify network connectivity
   - Ensure proper rate limit handling

2. **Performance Issues**
   - Monitor resource usage
   - Optimize database queries
   - Implement caching for frequent operations

3. **UI Rendering Problems**
   - Check browser compatibility
   - Verify frontend build process
   - Test responsive design on different devices

### Diagnostic Tools

1. **Logging**
   - Check application logs for errors
   - Monitor LLM API request logs
   - Track performance metrics

2. **Monitoring**
   - Set up alerts for API failures
   - Monitor system resource usage
   - Track user engagement metrics

## Conclusion

This deployment guide provides comprehensive instructions for deploying the Psycho-Color Analysis System in various environments. By following these guidelines, you can ensure a smooth deployment process and optimal system performance.

For additional support or custom deployment scenarios, please contact our support team at support@psycho-color-analysis.com.
