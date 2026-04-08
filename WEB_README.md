# AI Legal Monitoring System - Web Dashboard

This directory contains the web interface for the AI Legal Monitoring System.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements-web.txt
```

### 2. Run the Web Application

```bash
python web_app.py
```

### 3. Access the Dashboard

Open your web browser and navigate to: http://localhost:5000

## Features

- **Real-time Dashboard**: View system metrics, alerts, and recommendations
- **Document Processing**: Process legal documents by URL
- **Interactive Charts**: Visualize compliance status, risk distribution, and activity trends
- **Alert Management**: View and manage active legal alerts
- **Audit Logging**: Track all system activities and changes
- **Responsive Design**: Works on desktop and mobile devices

## API Endpoints

The web application provides the following REST API endpoints:

- `GET /api/dashboard` - Get dashboard overview data
- `GET /api/documents` - Get processed documents
- `GET /api/alerts` - Get active alerts
- `GET /api/recommendations` - Get pending recommendations
- `GET /api/audit-logs` - Get audit logs
- `POST /api/process-document` - Process a new document

## File Structure

```
AI-Legal-Monitoring/
├── web_app.py              # Flask web server
├── requirements-web.txt    # Web app dependencies
├── templates/
│   └── index.html         # Main dashboard template
├── static/
│   ├── css/
│   │   └── styles.css     # Dashboard styling
│   └── js/
│       ├── app.js         # Main application logic
│       └── charts.js      # Chart.js visualizations
└── src/                   # Backend modules (imported)
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, you can change the port in `web_app.py`:

```python
app.run(host='localhost', port=8000, debug=True)
```

### Missing Dependencies
If you encounter import errors, make sure all dependencies are installed:

```bash
pip install --upgrade -r requirements-web.txt
```

### Static Files Not Loading
Make sure Flask can find the static files. The directory structure should be:

```
AI-Legal-Monitoring/
├── static/
├── templates/
└── web_app.py
```

## Development

To modify the dashboard:

1. **HTML Template**: Edit `templates/index.html`
2. **Styling**: Edit `static/css/styles.css`
3. **JavaScript**: Edit `static/js/app.js` and `static/js/charts.js`
4. **Backend API**: Edit `web_app.py`

After making changes, restart the Flask server to see the updates.

## Integration with Backend

The web application imports and uses the backend modules from the `src/` directory. Make sure the backend system is properly configured and all dependencies are installed before running the web app.