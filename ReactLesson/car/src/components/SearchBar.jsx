import {useState} from 'react';

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
        <div>
            <form onSubmit={handleFormSubmit}>
                <input value={term} onChange={handleChange} />
                {/* {term.length < 3 && 'Term must be longer'} */}
            </form>
        </div>
    );
}