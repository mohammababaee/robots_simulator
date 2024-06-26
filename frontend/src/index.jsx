import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, TableContainer, TableHead, TableBody, TableRow, TableCell, Paper } from '@mui/material';

const SensorDataList = () => {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/sensor-data');
        setSensorData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Hub ID</TableCell>
            <TableCell>Temperature</TableCell>
            <TableCell>Humidity</TableCell>
            <TableCell>Timestamp</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {sensorData.map((dataEntry, index) => (
            <TableRow key={index}>
              <TableCell>{dataEntry.hub_id}</TableCell>
              <TableCell>{dataEntry.temperature}</TableCell>
              <TableCell>{dataEntry.humidity}</TableCell>
              <TableCell>{dataEntry.timestamp}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default SensorDataList;
