
import Cookies from "js-cookie";

const BASE_URL = "http://127.0.0.1:8000";
export const getAllMembers = async (params = {}) => {
  const token = Cookies.get("sub");

  const { first_name, status, page = 1, per_page = 20 } = params;

  const queryParams = new URLSearchParams();

  if (first_name) {
    queryParams.append("first_name", first_name);
  }

  if (status) {
    queryParams.append("status", status);
  }

  queryParams.append("page", page);
  queryParams.append("per_page", per_page);

  const url = `${BASE_URL}/members/?${queryParams.toString()}`;

  try {
    const response = await fetch(url, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error("Failed to fetch members");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    throw error;
  }
};
