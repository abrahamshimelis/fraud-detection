import React, { useState } from 'react';
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  MenuItem,
} from '@mui/material';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    user_id: '',
    signup_time: '',
    purchase_time: '',
    purchase_value: '',
    device_id: '',
    source: '',
    browser: '',
    sex: '',
    age: '',
    ip_address: '',
    country: '',
  });
  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      if (data.prediction = 0) {
        setPrediction("No fraudulent activity detected")
      } else {
        setPrediction("Potential fraudulent activity detected")
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <Container maxWidth="sm" sx={{p:10}}>
      <Box mt={5}>
        <Typography variant="h4" gutterBottom>
          Fraud Detection Prediction
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            margin="normal"
            label="User ID"
            name="user_id"
            value={formData.user_id}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Signup Time"
            name="signup_time"
            type="datetime-local"
            InputLabelProps={{ shrink: true }}
            value={formData.signup_time}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Purchase Time"
            name="purchase_time"
            type="datetime-local"
            InputLabelProps={{ shrink: true }}
            value={formData.purchase_time}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Purchase Value"
            name="purchase_value"
            type="number"
            value={formData.purchase_value}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Device ID"
            name="device_id"
            value={formData.device_id}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Source"
            name="source"
            value={formData.source}
            onChange={handleChange}
            select
          >
            <MenuItem value="SEO">SEO</MenuItem>
            <MenuItem value="Ads">Ads</MenuItem>
            <MenuItem value="Referral">Referral</MenuItem>
          </TextField>
          <TextField
            fullWidth
            margin="normal"
            label="Browser"
            name="browser"
            value={formData.browser}
            onChange={handleChange}
            select
          >
            <MenuItem value="chrome">Chrome</MenuItem>
            <MenuItem value="firefox">Firefox</MenuItem>
            <MenuItem value="safari">Safari</MenuItem>
          </TextField>
          <TextField
            fullWidth
            margin="normal"
            label="Sex"
            name="sex"
            value={formData.sex}
            onChange={handleChange}
            select
          >
            <MenuItem value="M">Male</MenuItem>
            <MenuItem value="F">Female</MenuItem>
          </TextField>
          <TextField
            fullWidth
            margin="normal"
            label="Age"
            name="age"
            type="number"
            value={formData.age}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="IP Address"
            name="ip_address"
            value={formData.ip_address}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Country"
            name="country"
            value={formData.country}
            onChange={handleChange}
          />
          <Button
            fullWidth
            variant="contained"
            color="primary"
            type="submit"
            sx={{ mt: 3 }}
          >
            Predict
          </Button>
        </form>
        {prediction !== null && (
          <Box mt={3}>
            <Typography variant="h6">Prediction Result:</Typography>
            <Typography variant="body1">{prediction}</Typography>
          </Box>
        )}
      </Box>
    </Container>
  );
}

export default App;
