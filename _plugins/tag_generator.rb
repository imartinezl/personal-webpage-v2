Jekyll::Hooks.register :projects, :post_write do |post|
    all_existing_tags = Dir.entries("_tags")
      .map { |t| t.match(/(.*).md/) }
      .compact.map { |m| m[1] }
  
    tags = post['tags'].reject { |t| t.empty? }
    tags.each do |tag|
      generate_tag_file(tag) if !all_existing_tags.include?(tag)
    end
  end
  
  def generate_tag_file(tag)
    tag_slug = tag.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
    File.open("_tags/#{tag_slug}.md", "wb") do |file|
      file << "---\nlayout: tags\ntag-name: #{tag}\n---\n"
    end
  end