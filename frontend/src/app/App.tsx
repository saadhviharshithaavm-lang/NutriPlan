import { BrowserRouter, Route, Routes } from 'react-router'

import { AppLayout } from '../components/layout/AppLayout'
import { AdminPage } from '../pages/AdminPage'
import { DashboardPage } from '../pages/DashboardPage'
import { GroceryListPage } from '../pages/GroceryListPage'
import { LandingPage } from '../pages/LandingPage'
import { LoginPage } from '../pages/LoginPage'
import { MealDetailsPage } from '../pages/MealDetailsPage'
import { MealPlanPage } from '../pages/MealPlanPage'
import { NotFoundPage } from '../pages/NotFoundPage'
import { ProfilePage } from '../pages/ProfilePage'
import { RegisterPage } from '../pages/RegisterPage'

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route index element={<LandingPage />} />
          <Route path="login" element={<LoginPage />} />
          <Route path="register" element={<RegisterPage />} />
          <Route path="profile" element={<ProfilePage />} />
          <Route path="meal-plan" element={<MealPlanPage />} />
          <Route path="meal-plan/:recipeId" element={<MealDetailsPage />} />
          <Route path="grocery-list" element={<GroceryListPage />} />
          <Route path="dashboard" element={<DashboardPage />} />
          <Route path="admin" element={<AdminPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
