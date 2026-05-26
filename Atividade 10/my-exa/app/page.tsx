"use client";

import './globals.css';
import React, { useState, useEffect } from 'react';

interface Message {
  Author: string;
  Message: string;
  Date: string;
}

interface MessageRowProps {
  message: Message;
}

interface MessageTableProps {
  messages: Message[];
  filterText: string;
}

interface SearchBarProps {
  filterText: string;
  onFilterTextChange: (text: string) => void;
}

interface FilterableMessageTableProps {
  messages: Message[];
}

function MessageRow({ message }: MessageRowProps) {
  return (
    <tr>
      <td>{message.Author}</td>
      <td>{message.Message}</td>
      <td>{message.Date}</td>
    </tr>
  );
}

function MessageTable({ messages, filterText }: MessageTableProps) {
  const rows: React.ReactNode[] = [];

  messages.forEach((message, index) => {
    const author = message.Author || '';
    const content = message.Message || '';
    const query = filterText || '';

    if (
      author.toLowerCase().indexOf(query.toLowerCase()) === -1 &&
      content.toLowerCase().indexOf(query.toLowerCase()) === -1
    ) {
      return;
    }

    rows.push(
      <MessageRow
        key={`${message.Author}-${index}`}
        message={message}
      />
    );
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Author</th>
          <th>Message</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        {rows.length > 0 ? (
          rows
        ) : (
          <tr>
            <td colSpan={3} style={{ textAlign: 'center', padding: '16px', color: '#666' }}>
              No messages found.
            </td>
          </tr>
        )}
      </tbody>
    </table>
  );
}

function SearchBar({ filterText, onFilterTextChange }: SearchBarProps) {
  return (
    <form>
      <input 
        type="text" 
        value={filterText} 
        placeholder="Search..."
        onChange={(e) => onFilterTextChange(e.target.value)} 
      />
    </form>
  );
}

function FilterableMessageTable({ messages }: FilterableMessageTableProps) {
  const [filterText, setFilterText] = useState('');
  return (
    <div>
      <SearchBar 
        filterText={filterText}
        onFilterTextChange={setFilterText} 
      />
      
      <MessageTable
        messages={messages} 
        filterText={filterText} 
      />
    </div>
  );
}

export default function Home() {
  const [blogMessages, setBlogMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://script.googleusercontent.com/macros/echo?user_content_key=AUkAhnThfjPLRbuagvryfh8J_uo_eJLtQDsSBzc-vAdBwaDm7-ViiItToVBkC17yWKRxHFXUBSatE75Extb9u3jyQ1XMXQiu6PzxWkqJgpDUXuNv0e6ODO2vcGeeHqkiDIAg39QEY_wvxL0pAd7gKimTqzo6yWi9L08ooZ0zkTjMAm0FiaE0aG7r5cCHjK8Hl70zNaYqT9qkxbiwZCS3i3ePjKIoYY5G_kmO2LYzMzapkGuJBBQMA9UBDqKJISCfiFpSL5pJLiXQs2tOdFjApk14B3xN9Q6FSQ&lib=Mc7gKNDFWsXKUX18VxT19L_g9uKiEqo84')
      .then(response => response.json())
      .then((data: any[][]) => {
        const formatted = data.map((item) => ({
          Message: String(item[0] ?? ''),
          Author: String(item[1] ?? ''),
          Date: String(item[2] ?? '')
        }));
        setBlogMessages(formatted);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to load blog messages:", err);
        setLoading(false);
      });
  }, []); // Run only once when the component mounts

  return (
    <main>
      {loading ? (
        <p style={{ textAlign: 'center', padding: '20px' }}>Loading messages...</p>
      ) : (
        <FilterableMessageTable messages={blogMessages} />
      )}
    </main>
  );
}