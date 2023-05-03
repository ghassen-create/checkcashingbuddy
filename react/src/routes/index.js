import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import AuthSimpleLayout from '../layouts/AuthSimpleLayout';
import MainLayout from '../layouts/MainLayout';
import ErrorLayout from '../layouts/ErrorLayout';

import Starter from 'components/pages/Starter';
import Profile from 'components/pages/user/profile/Profile';
import Settings from 'components/pages/user/settings/Settings';
import AdvanceTableExamples from 'components/doc-components/AdvanceTableExamples';
import Customers from 'components/app/e-commerce/customers/Customers';

import Error404 from 'components/errors/Error404';

import CardLogin from 'components/authentication/card/Login';
import Logout from 'components/authentication/card/Logout';
import CardRegistration from 'components/authentication/card/Registration';
import CardForgetPassword from 'components/authentication/card/ForgetPassword';
import CardConfirmMail from 'components/authentication/card/ConfirmMail';
import CardPasswordReset from 'components/authentication/card/PasswordReset';
import CardLockScreen from 'components/authentication/card/LockScreen';

const FalconRoutes = () => {
  return (
    <Routes>
      <Route exact path="/" element={<></>} />
      <Route element={<ErrorLayout />}>
        <Route path="errors/404" element={<Error404 />} />
      </Route>
      {/*- ------------- Authentication ---------------------------  */}

      {/*- ------------- Card ---------------------------  */}
      <Route path="/login" element={<CardLogin />} />
      <Route
        path="/register"
        element={<CardRegistration />}
      />
      <Route path="/logout" element={<Logout />} />
      <Route
        path="/forgot-password"
        element={<CardForgetPassword />}
      />
      <Route
        path="/reset-password"
        element={<CardPasswordReset />}
      />
      <Route
        path="/confirm-mail"
        element={<CardConfirmMail />}
      />
      <Route
        path="/lock-screen"
        element={<CardLockScreen />}
      />

      {/*- ------------- Split ---------------------------  */}

      {/* //--- MainLayout Starts  */}

      <Route element={<MainLayout />}>
        <Route path="/customer" element={<Customers />} />
        <Route path="/user" element={<Customers />} />

        {/*Pages*/}
        <Route path="pages/starter" element={<Starter />} />
        <Route path="/settings" element={<Settings />} />
        <Route
          path="tables/advance-tables"
          element={<AdvanceTableExamples />}
        />
      </Route>

      {/* //--- MainLayout end  */}

      {/* <Navigate to="/errors/404" /> */}
      <Route path="*" element={<Navigate to="/errors/404" replace />} />
    </Routes>
  );
};

export default FalconRoutes;
