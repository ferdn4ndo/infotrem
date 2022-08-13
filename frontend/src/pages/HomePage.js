import { useEffect } from 'react';
import PageHeader from '../components/PageHeader/PageHeader';
import Container from '@mui/material/Container';
import { ConfigClient, API_BASE_URL } from '../config/ConfigClient';
import { observer } from "mobx-react";
import { useStore } from "../store/useStore";
import { values } from 'mobx';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';

const HomePage = observer(() => {
  const store = useStore();

  useEffect(() => {
    store.fetchMonitors().then(() => {
      values(store.monitors).forEach((monitor) => {
        monitor.fetchMetrics();
      });
    });
  }, []);

  return (
    <>
      <PageHeader />
      <Container maxWidth="md">
        <div>HomePage: {ConfigClient.get(API_BASE_URL)}</div>
        {store.loadingMonitors &&
          <CircularProgress />
        }
        {!store.loadingMonitors &&
          <p>Done! {store.loadingMonitors}</p>
        }
        <div>
          {values(store.monitors).map((monitor, monitorIndex) => (
            <Accordion key={monitor.id}>
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls={`panel${monitorIndex}-content`}
                id={`panel${monitorIndex}-header`}
              >
                <Typography>{monitor.name}</Typography>
                {monitor.loadingMetrics &&
                  <CircularProgress size={15} sx={{ml: 4}}/>
                }
              </AccordionSummary>
              <AccordionDetails>
                <Typography style={{whiteSpace: 'pre'}}>
                  {JSON.stringify(monitor.metrics, null, '\t')}
                </Typography>
              </AccordionDetails>
            </Accordion>
          ))}
        </div>
      </Container>
    </>
  );
});

export default HomePage
