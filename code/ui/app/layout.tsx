// app/layout.js
import '../styles/globals.css';
import '../styles/styles.css'; // 전역 스타일 (없다면 생략)


export const metadata = {
  title: 'Psycho-Color Analysis System',
  description: 'Discover your personality traits through color preferences',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1"
        />
        {/* Bootstrap CSS */}
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
          rel="stylesheet"
        />
      </head>
      <body>
        {children}
        {/* Bootstrap Bundle, SortableJS, Chart.js, jsPDF */}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/sortablejs@1.14.0/Sortable.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        {/* 기존 app.js */}
        <script src="/app.js"></script>
      </body>
    </html>
  );
}
