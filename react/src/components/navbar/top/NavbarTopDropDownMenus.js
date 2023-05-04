import React from 'react';
import NavbarDropdown from './NavbarDropdown';
import {
  pagesRoutes
} from 'routes/siteMaps';
import NavbarDropdownPages from './NavbarDropdownPages';

const NavbarTopDropDownMenus = () => {
  return (
    <>
      <NavbarDropdown title="pages">
        <NavbarDropdownPages items={pagesRoutes.children} />
      </NavbarDropdown>
    </>
  );
};

export default NavbarTopDropDownMenus;
