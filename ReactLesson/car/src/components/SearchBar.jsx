import {useState} from 'react';
import  './SearchBar.css';

export const SearchBar = ({onSubmit}) => {
    const [term,setTerm] = useState('');

    const handleChange = (event) => {
       setTerm(event.target.value); 

    //    use to replace the smaller case entered string with empty string
    //    setTerm(event.target.value.replace(/[a-z]/,'')); 
    }

    const handleFormSubmit = (event) => {
        event.preventDefault();
        setTerm(''); //clear state after input
        onSubmit(term);
    };
    
    return(
        <div className='search-bar'>
            <form onSubmit={handleFormSubmit}>
                <label> Enter Search term</label>
                <input value={term} onChange={handleChange} />
                {/* {term.length < 3 && 'Term must be longer'} */}
            </form>
        </div>
    );
}