import {SearchBar} from './components/SearchBar';
import './App.css'

function App() {
  const handleSubmit = (term) => {
    console.log("Do a search with",term);
    // SearchBar(term);
  }

  return (
    <>
      <div>
        <SearchBar onSubmit={handleSubmit} />
      </div>
    </>
  )
}

export default App
