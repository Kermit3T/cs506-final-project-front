import { useState } from 'react'
import styled from 'styled-components'
import ImageUpload from './components/ImageUpload'
import Results from './components/Results'
import { GlobalStyle } from './styles/GlobalStyle'

const AppContainer = styled.div`
  width: 100%;
  min-height: 100vh;
  margin: 0 auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;

  /* Mobile devices */
  max-width: 100%;

  /* Tablet devices */
  @media (min-width: 640px) {
    max-width: 90%;
    padding: 1.5rem;
  }

  /* Laptop devices */
  @media (min-width: 1024px) {
    max-width: 80%;
    padding: 2rem;
  }

  /* Desktop devices */
  @media (min-width: 1280px) {
    max-width: 1200px;
  }
`

const Title = styled.h1`
  color: #2c3e50;
  text-align: center;
  margin-bottom: 2rem;
`

const Disclaimer = styled.div`
  background-color: #fff3cd;
  border: 1px solid #ffeeba;
  color: #856404;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 2rem;
`

const ErrorMessage = styled.div`
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  color: #721c24;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
`

function App() {
  const [results, setResults] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleAnalysis = async (imageFile) => {
    try {
      setIsLoading(true)
      setError(null)
      
      // For testing - remove this when you have a real API
      console.log('Analyzing image:', imageFile)
      
      // Simulated API call - replace this with your actual API endpoint
      await new Promise(resolve => setTimeout(resolve, 2000)) // Simulate 2 second delay
      
      // Temporary mock results - replace this with your actual API call
      const mockResults = {
        classification: "Test Classification",
        confidence: 0.95,
        details: "This is a test result"
      }
      setResults(mockResults)
      
      /* Uncomment this when you have your API ready
      const formData = new FormData()
      formData.append('image', imageFile)

      const response = await fetch('http://your-api-endpoint/analyze', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Analysis failed')
      }

      const data = await response.json()
      setResults(data)
      */
      
    } catch (err) {
      console.error('Analysis error:', err)
      setError('Analysis failed: ' + (err.message || 'Unknown error'))
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <>
      <GlobalStyle />
      <AppContainer>
        <Title>Cancer Cell Detection Analysis</Title>
        <Disclaimer>
          <strong>Medical Disclaimer:</strong> This tool is for research and preliminary screening purposes only. 
          It should not be used as a primary diagnostic tool. Always consult with qualified healthcare professionals 
          for medical diagnosis and advice.
        </Disclaimer>
        <ImageUpload onUpload={handleAnalysis} isLoading={isLoading} />
        {error && <ErrorMessage>{error}</ErrorMessage>}
        {results && <Results data={results} />}
      </AppContainer>
    </>
  )
}

export default App