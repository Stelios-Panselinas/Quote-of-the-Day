const quoteText = document.getElementById('quoteText');
const quoteAuthor = document.getElementById('quoteAuthor');
const newQuoteBtn = document.getElementById('newQuoteBtn');
const currentDate = document.getElementById('currentDate');

function displayDate() {
  const today = new Date();
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  currentDate.textContent = today.toLocaleDateString('en-US', options);
}

async function fetchQuote() {
  try {
    // Disable button while fetching
    newQuoteBtn.disabled = true;
    newQuoteBtn.textContent = 'Loading...';

    // Use our backend API endpoint instead of directly calling the external API
    fetch('https://api.quotable.io/random')
      .then(response =>{
        if(!response.ok){
          throw new Error('Failed to fetch quote');
        }
        return response.json();
      })
    .then(
      data =>{
        quoteText.textContent = data.content;
        quoteAuthor.textContent = data.author;
      }
    )
    
    if (!response.ok) {
      throw new Error('Failed to fetch quote');
    }

    const data = await response.json();
    
    // Update quote text and author
  //   quoteText.textContent = data.content;
  //   quoteAuthor.textContent = data.author;

  // } catch (error) {
  //   quoteText.textContent = 'Failed to load quote. Please try again.';
  //   quoteAuthor.textContent = '';
  //   console.error('Error fetching quote:', error);
  // 
  } finally {
    // Re-enable button
    newQuoteBtn.disabled = false;
    newQuoteBtn.textContent = 'New Quote';
  }
}

// Add click event listener to button
newQuoteBtn.addEventListener('click', fetchQuote);

// Load date and quote when page first loads
window.addEventListener('load', () => {
  displayDate();
  fetchQuote();
});
