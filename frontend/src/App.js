import { Provider } from "mobx-react";
import { createStore } from "./store/createStore";
import HomePage from './pages/HomePage';
import { ThemeProvider } from '@mui/material';
import { createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const store = createStore();

function App() {
  return (
    <Provider store={store}>
      <CssBaseline />
      <ThemeProvider theme={createTheme({})}>
        <HomePage />
      </ThemeProvider>
    </Provider>
  );
}

export default App;
