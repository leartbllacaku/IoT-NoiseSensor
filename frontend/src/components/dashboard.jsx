import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { Line } from 'react-chartjs-2';
import 'bootstrap/dist/css/bootstrap.min.css';
import './dashboard.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Register the components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/data')  // Update the endpoint to /data
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("Error fetching data", error));
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  const chartData = {
    labels: data.timestamps,
    datasets: [
      {
        label: 'Noise Levels',
        data: data.noise_levels,
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  return (
    <Container className='dashboard-container'>
      <Row className="justify-content-center mt-3">
        <Col md={8} lg={6}>
          <Card>
            <Card.Body>
              <Card.Title>Noise Monitoring Dashboard</Card.Title>
              <Line data={chartData} />
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Dashboard;