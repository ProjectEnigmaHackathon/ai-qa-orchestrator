import { Routes, Route } from 'react-router-dom'
import ChatPage from '@/pages/ChatPage'
import SettingsPage from '@/pages/SettingsPage'
import Layout from '@/components/Layout'
import ErrorBoundary from '@/components/ErrorBoundary'
import { AppProvider, RepositoryProvider } from '@/context'

function App() {
  return (
    <ErrorBoundary>
      <AppProvider>
        <RepositoryProvider>
          <Layout>
            <Routes>
              <Route path="/" element={<ChatPage />} />
              <Route path="/settings" element={<SettingsPage />} />
            </Routes>
          </Layout>
        </RepositoryProvider>
      </AppProvider>
    </ErrorBoundary>
  )
}

export default App