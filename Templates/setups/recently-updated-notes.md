<%*
try {
    // Get current file
    const currentFile = tp.file.find_tfile(tp.file.title);
    if (!currentFile) throw new Error("Current file not found");
    
    // Get existing content first
    const existingContent = await app.vault.read(currentFile);
    
    // Get Dataview API
    const dv = app.plugins.plugins["dataview"].api;
    if (!dv) throw new Error("Dataview API not found");
    
    const query = `TABLE WITHOUT ID
    title AS "Title",
    author AS "Author",
    created AS "Created",
    published AS "Published",
    tags AS "Tags"
    FROM ""
    SORT file.ctime DESC
    LIMIT 10`;
    
    const queryOutput = await dv.queryMarkdown(query);
    const timestamp = moment().format('YYYY-MM-DD HH:mm');
    
    // Combine existing content with new content
    const newContent = existingContent + 
        (existingContent ? '\n\n' : '') +
        `## Updated ${timestamp}\n${queryOutput.value}`;
    
    await app.vault.modify(currentFile, newContent);
    
    new Notice("Content successfully updated");
    
} catch (error) {
    console.error("Template Error:", error);
    new Notice("Failed to update content: " + error.message);
}
_%>
