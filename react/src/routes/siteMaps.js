export const pagesRoutes = [
    {
        label: 'pages',
        children: [
            {
                name: 'Accounts',
                icon: 'user',
                to: '/user',
                active: true,
            },
            {
                name: 'Customers',
                icon: 'users',
                to: '/customer',
                active: true,
            },
            {
                name: 'Checks',
                icon: 'dollar-sign',
                active: true,
                children: [
                    {
                        name: 'Checks',
                        to: '/check',
                        active: true,
                    },
                    {
                        name: 'Checks Logs',
                        to: '/check-logs',
                        active: true,
                    },
                ]
            },
            {
                name: 'Store',
                icon: "shopping-cart",
                to: '/store',
                active: true,
            },
            {
                name: 'Report',
                icon: "chart-pie",
                to: '/report',
                active: true,
            },
        ]
    }
];

export default pagesRoutes
