#!/bin/bash
# Test script to verify the unified Flask instance is working correctly

echo "Testing Flask application..."
echo "========================================"

# Test if Flask is running
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/)

if [ "$response" = "200" ]; then
    echo "✓ Flask is running on port 5000"
    
    # Test if landing page loads
    landing=$(curl -s http://localhost:5000/ | grep -o "Escolha o Sistema" | head -1)
    if [ ! -z "$landing" ]; then
        echo "✓ Landing page (/) is working"
    else
        echo "✗ Landing page (/) is NOT working properly"
    fi
    
    # Test if login pages exist
    vivo_login=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/vivo/login)
    claro_login=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/claro/login)
    
    if [ "$vivo_login" = "200" ]; then
        echo "✓ Vivo login page (/vivo/login) is working"
    else
        echo "✗ Vivo login page (/vivo/login) returned: $vivo_login"
    fi
    
    if [ "$claro_login" = "200" ]; then
        echo "✓ Claro login page (/claro/login) is working"
    else
        echo "✗ Claro login page (/claro/login) returned: $claro_login"
    fi
    
    echo "========================================"
    echo "All tests completed!"
else
    echo "✗ Flask is NOT running on port 5000"
    echo "Response code: $response"
fi
