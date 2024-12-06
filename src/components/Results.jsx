import styled from 'styled-components'

const ResultsContainer = styled.div`
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f7fafc;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`

const ResultItem = styled.div`
  margin: 0.5rem 0;
  display: flex;
  justify-content: space-between;
`

const Results = ({ data }) => {
  return (
    <ResultsContainer>
      <h2>Analysis Results</h2>
      <ResultItem>
        <span>Classification:</span>
        <strong>{data.classification}</strong>
      </ResultItem>
      <ResultItem>
        <span>Confidence:</span>
        <strong>{(data.confidence * 100).toFixed(2)}%</strong>
      </ResultItem>
      {data.details && (
        <ResultItem>
          <span>Additional Details:</span>
          <p>{data.details}</p>
        </ResultItem>
      )}
    </ResultsContainer>
  )
}

export default Results