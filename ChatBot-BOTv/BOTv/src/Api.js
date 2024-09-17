export const postData = async (url = '', data = {data:"ex"}) => {
    
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), 
      });
 
      if (!response.ok) {
        throw new Error('Response was not ok');
      }
  
      const result = await response.json(); 
      console.log(result)

      return result;
     
  };