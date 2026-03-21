/**
 * Main application JavaScript
 * Add your client-side logic here
 */

console.log('FastAPI Template loaded successfully!');

// Example: Fetch health check on page load
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        console.log('Health check:', data);
    } catch (error) {
        console.error('Health check failed:', error);
    }
});

// Example: Fetch and display items
async function fetchItems() {
    try {
        const response = await fetch('/api/items');
        const items = await response.json();
        console.log('Items:', items);
        return items;
    } catch (error) {
        console.error('Failed to fetch items:', error);
        return [];
    }
}

// Example: Create a new item
async function createItem(itemData) {
    try {
        const response = await fetch('/api/items', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(itemData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const item = await response.json();
        console.log('Created item:', item);
        return item;
    } catch (error) {
        console.error('Failed to create item:', error);
        throw error;
    }
}

// Example usage (commented out):
// fetchItems().then(items => {
//     console.log('All items:', items);
// });

// createItem({
//     name: 'New Item',
//     description: 'Created from JavaScript',
//     price: 39.99,
//     is_available: true
// }).then(item => {
//     console.log('Successfully created:', item);
// });
