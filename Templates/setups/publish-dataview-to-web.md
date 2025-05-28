<%*
try {
    // Get current file and verify it exists
    const currentFile = tp.file.find_tfile(tp.file.title);
    if (!currentFile) throw new Error("Current file not found");
    
    // Get Dataview API
    const dv = app.plugins.plugins["dataview"].api;
    if (!dv) throw new Error("Dataview API not found");
    
    // Read existing content
    const existingContent = await app.vault.read(currentFile);
    
    // Create the query with specific file path
    const query = `TABLE WITHOUT ID
    title AS "Title",
    author AS "Author",
    created AS "Created",
    published AS "Published",
    join(map(tags, (t) => link("#" + t)), ", ") AS "Tags"
    WHERE file.path = "${currentFile.path}"`;
    
    // Execute query and get markdown output
    const queryOutput = await dv.queryMarkdown(query);
    
    let newContent;
    if (existingContent.startsWith('---')) {
        // Find the end of frontmatter
        const endFrontmatter = existingContent.indexOf('---', 3);
        if (endFrontmatter !== -1) {
            // Split content at end of frontmatter
            const frontMatter = existingContent.substring(0, endFrontmatter + 3);
            const remainingContent = existingContent.substring(endFrontmatter + 3);
            
            // Combine with new table after frontmatter
            newContent = frontMatter + '\n\n' + queryOutput.value + remainingContent;
        }
    } else {
        // If no frontmatter, prepend table
        newContent = queryOutput.value + '\n\n' + existingContent;
    }
    
    // Write to the current file
    await app.vault.modify(currentFile, newContent);
    
    new Notice("Table inserted after frontmatter");
} catch (error) {
    console.error("Template Error:", error);
    new Notice("Failed to insert table: " + error.message);
}
_%>

