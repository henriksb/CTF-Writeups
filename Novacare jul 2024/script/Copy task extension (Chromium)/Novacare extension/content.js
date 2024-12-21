if (document.location.href.includes("https://kodekalender.novacare.no/luke")) {
    // Extract the task content
    const taskElement = document.querySelector(".question");
    
    if (taskElement) {
      const taskContent = taskElement.innerText;
  
      // Extract all links within the task description
      const links = Array.from(taskElement.querySelectorAll("a"))
        .map(link => link.href)
        .join("\n");
  
      // Combine task content and links
      const combinedContent = `${taskContent}\n\nLinks:\n${links || "No links found."}`;
  
      // Copy the combined content to the clipboard
      navigator.clipboard.writeText(combinedContent).then(() => {
        console.log("Task content and links copied to clipboard:", combinedContent);
      }).catch(err => {
        console.error("Failed to copy task content and links:", err);
      });
    } else {
      console.warn("No task content found on this page.");
    }
  }
  