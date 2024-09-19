import react from 'react'


const GrafanaDashboard = () => {
    return (
      <div style={{ width: '100%', height: '100vh' }}>
        <iframe
          src="https://your-grafana-instance/d/your_dashboard_id?orgId=1&kiosk"
          width="100%"
          height="100%"
          frameBorder="0"
          title="Grafana Dashboard"
        ></iframe>
      </div>
    );
  };
  
  export default GrafanaDashboard;