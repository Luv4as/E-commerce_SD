import React from 'react'
import ReactDOM from 'react-dom/client'
import Home from './pages/Home.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import SobreNos from './pages/SobreNos.jsx'
import './styles.css'
import Layout from './componentes/Layout.jsx'
import Cadastro from './pages/Cadastro.jsx'
import Login from './pages/Login.jsx'
import Categoria from './pages/Categoria.jsx'

const router = createBrowserRouter([
  {
    path:'/',
    element: <Home/>
  },
  {
    path:'/sobrenos',
    element: <SobreNos/>
  },
  {
    path:'/login',
    element: <Login/>
  },
  {
    path:'/cadastro',
    element: <Cadastro/>
  },
  {
    path:'/categoria/:categoria',
    element: <Categoria/>
  },
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Layout> 
      <RouterProvider router={router}/>
    </Layout>
  </React.StrictMode>,
)
