import React, { useState } from 'react'

function App() {
  const [url, setUrl] = useState('')
  const [metadata, setMetadata] = useState(null)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setMetadata(null)

    try {
      const response = await fetch('http://127.0.0.1:5000/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      })

      const data = await response.json()
      if (!response.ok) throw new Error(data.error || 'Something went wrong')

      setMetadata(data)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h2>URL Metadata and Transcript Extractor</h2>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          placeholder='Enter YouTube URL'
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ width: '300px', padding: '8px' }}
          required
        />
        <button
          type='submit'
          style={{ marginLeft: '10px', padding: '8px 15px' }}
        >
          Fetch Data
        </button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {metadata && (
        <div style={{ marginTop: '20px' }}>
          <h3>{metadata.title}</h3>
          <p>{metadata.description}</p>
          {metadata.image && metadata.image !== 'No image found' && (
            <img src={metadata.image} alt='Preview' width='300' />
          )}
          {metadata.transcript && (
            <div
              style={{ textAlign: 'left', margin: '20px auto', width: '60%' }}
            >
              <h4>Transcript:</h4>
              <p style={{ whiteSpace: 'pre-wrap' }}>{metadata.transcript}</p>
            </div>
          )}

          {metadata.tweets && (
            <div
              style={{
                textAlign: 'left',
                margin: '20px auto',
                width: '60%',
                border: '1px solid #ddd',
                padding: '10px',
                borderRadius: '5px',
              }}
            >
              <h4>Generated Tweet Thread:</h4>
              {metadata.tweets.map((tweet, index) => (
                <p key={index} style={{ marginBottom: '10px' }}>
                  {tweet}
                </p>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default App
