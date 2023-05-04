import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';
import ErrorLayout from '../layouts/ErrorLayout';

import Settings from '../pages/Users/settings/Settings';
import Customers from '../pages/Customers/Customers';
import Users from '../pages/Users/Users';

import Error404 from '../pages/errors/Error404';

import CardLogin from '../pages/authentication/card/Login';
import Logout from '../pages/authentication/card/Logout';
import CardForgetPassword from '../pages/authentication/card/ForgetPassword';
import CardConfirmMail from '../pages/authentication/card/ConfirmMail';
import CardPasswordReset from '../pages/authentication/card/PasswordReset';
import CardLockScreen from '../pages/authentication/card/LockScreen';
import Check from "../pages/Checks/Checks/Check";
import CheckLogs from "../pages/Checks/Logs/CheckLogs";
import Store from "../pages/Store/Store";
import Report from "../pages/Report/Report";

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
        <Route path="/user" element={<Users />} />
        <Route path="/check" element={<Check />} />
        <Route path="/check-logs" element={<CheckLogs />} />
        <Route path="/store" element={<Store />} />
        <Route path="/report" element={<Report />} />

        {/*Pages*/}
        <Route path="/settings" element={<Settings />} />
      </Route>

      {/* //--- MainLayout end  */}

      {/* <Navigate to="/errors/404" /> */}
      <Route path="*" element={<Navigate to="/errors/404" replace />} />
    </Routes>
  );
};

export default FalconRoutes;
