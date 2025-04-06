import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { createTheme, ThemeProvider } from '@mui/material/styles';

// Create a custom theme
const theme = createTheme({
  components: {
    MuiTableCell: {
      styleOverrides: {
        head: {
          fontWeight: 'bold',
          backgroundColor: '#1976d2',
          color: 'white',
        },
        body: {
          fontSize: '0.875rem',
        },
      },
    },
  },
});

function createData(firstName, lastName, email, enrollment) {
  return { firstName, lastName, email, enrollment };
}

const rows = [
  createData('John', 'Doe', 'john.doe@example.com', '2023-01-15'),
  createData('Jane', 'Smith', 'jane.smith@example.com', '2023-02-20'),
  createData('Michael', 'Johnson', 'm.johnson@example.com', '2023-03-10'),
  createData('Emily', 'Williams', 'emily.w@example.com', '2023-01-05'),
  createData('David', 'Brown', 'david.brown@example.com', '2023-04-12'),
];

export default function BasicTable() {
  return (
    <ThemeProvider theme={theme}>
      <TableContainer 
        component={Paper} 
        sx={{ 
          maxWidth: 1000, 
          margin: '2rem auto',
          boxShadow: 3,
          borderRadius: 2,
        }}
      >
        <Table aria-label="user table">
          <TableHead>
            <TableRow>
              <TableCell>First name</TableCell>
              <TableCell align="right">Last name</TableCell>
              <TableCell align="right">Email</TableCell>
              <TableCell align="right">Enrollment Date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row, index) => (
              <TableRow
                key={row.email}
                sx={{ 
                  '&:nth-of-type(odd)': { backgroundColor: '#f5f5f5' },
                  '&:hover': { backgroundColor: '#e3f2fd' },
                }}
              >
                <TableCell>{row.firstName}</TableCell>
                <TableCell align="right">{row.lastName}</TableCell>
                <TableCell align="right" sx={{ fontStyle: 'italic' }}>{row.email}</TableCell>
                <TableCell align="right">{row.enrollment}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </ThemeProvider>
  );
}