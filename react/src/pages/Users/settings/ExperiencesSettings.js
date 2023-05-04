import React, { useState } from 'react';
import { Card } from 'react-bootstrap';
import FalconCardHeader from 'components/common/FalconCardHeader';
import ExperienceForm from './ExperienceForm';

const ExperiencesSettings = () => {
  const [collapsed, setCollapsed] = useState(false);
  return (
    <Card className="mt-3">
      <FalconCardHeader title="Experiences" />
      <Card.Body className="fs--1 bg-light">
        <ExperienceForm collapsed={collapsed} setCollapsed={setCollapsed} />
      </Card.Body>
    </Card>
  );
};

export default ExperiencesSettings;
