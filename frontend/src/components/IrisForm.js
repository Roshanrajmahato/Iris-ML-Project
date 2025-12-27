
// IrisForm.js
import React, { useState } from 'react';
import axios from 'axios';


export default function IrisForm() {
const [form, setForm] = useState({
sepal_length: '',
sepal_width: '',
petal_length: '',
petal_width: ''
});
const [result, setResult] = useState(null);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);


const handleChange = (e) => {
setForm({ ...form, [e.target.name]: e.target.value });
}


const handleSubmit = async (e) => {
e.preventDefault();
setLoading(true);
setError(null);
setResult(null);
try {
const resp = await axios.post('/predict', form);
setResult(resp.data);
} catch (err) {
setError(err.response?.data?.error || err.message);
} finally {
setLoading(false);
}
}


return (
<div style={{maxWidth:600, margin:'0 auto'}}>
<h2>Iris Prediction</h2>
<form onSubmit={handleSubmit}>
{Object.keys(form).map((k) => (
<div key={k} style={{marginBottom:10}}>
<label style={{display:'block', textTransform:'capitalize'}}>{k.replace('_',' ')}:</label>
<input
name={k}
value={form[k]}
onChange={handleChange}
required
step="any"
type="number"
style={{width:'100%', padding:8}}
/>
</div>
))}
<button type="submit" disabled={loading} style={{padding:'8px 16px'}}>
{loading ? 'Predicting...' : 'Predict'}
</button>
</form>


{error && <div style={{color:'red', marginTop:12}}>Error: {error}</div>}


{result && (
<div style={{marginTop:12}}>
<h3>Result</h3>
<p><strong>Prediction:</strong> {result.prediction} (index: {result.prediction_index})</p>
<p><strong>Probabilities:</strong> {result.probabilities.map((p,i)=>p.toFixed(3)).join(', ')}</p>
</div>
)}
</div>
);
}