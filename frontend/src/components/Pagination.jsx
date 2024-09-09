import React from 'react';
import './pagination.css';

const Pagination = ({ currentPage, totalPages, onPageChange }) => {
    const pageNumbers = [];

    for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i);
    }

    const handlePageClick = (pageNumber) => {
        onPageChange(pageNumber);
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    return (
        <div className="pagination">
            {pageNumbers.map(number => (
                <button
                    key={number}
                    onClick={() => handlePageClick(number)}
                    className={number === currentPage ? 'active' : ''}
                >
                    {number}
                </button>
            ))}
        </div>
    );
};

export default Pagination;
